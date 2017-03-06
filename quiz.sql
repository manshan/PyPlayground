5.
/* What vendor has the greatest number of distinct skus in the transaction table that do not exist in the skstinfo table? (Remember that vendors are listed as distinct numbers in our data set). */

select si.vendor, count(distinct si.sku) as vendor_skuinfo
from
(select distinct t.sku
from trnsact t left join skstinfo s
on t.sku = s.sku
where s.sku is null) as filter

join

skuinfo si

on filter.sku = si.sku
group by si.vendor
order by vendor_skuinfo desc;


/*Exercise 2. Use a CASE statement within an aggregate function to determine which sku
had the greatest total sales during the combined summer months of June, July, and August. */
select sku, sum(case when extract(month from saledate) = 6 then amt end) as June_amt,
sum(case when extract(month from saledate) = 7 then amt end) as July_amt,
sum(case when extract(month from saledate) = 8 then amt end) as Aug_amt,
(June_amt + July_amt + Aug_amt) as Combined_sale
from trnsact 
where stype = 'P'
group by sku
order by combined_sale desc;


/* Exercise 3. How many distinct dates are there in the saledate column of the transaction
table for each month/year/store combination in the database? Sort your results by the
number of days per combination in ascending order. */
select s.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem, count(distinct extract(day from t.saledate)) as Day_num
from trnsact t join strinfo s on t.store = s.store
group by salem, saley, s.store
order by salem, saley, s.store;

/* Exercise 4. What is the average daily revenue for each store/month/year combination in
the database? Calculate this by dividing the total revenue for a group by the number of
sales days available in the transaction table for that group.  */

select s.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct extract(day from t.saledate)) as Day_num, sum(amt) as monthR, (monthR/Day_num) as avgdailysale
from trnsact t join strinfo s on t.store = s.store
where t.stype = 'P'
group by s.store, salem, saley
having Day_num >= 20
order by s.store, salem, saley;

/* Exercise 5. What is the average daily revenue brought in by Dillard’s stores in areas of
high, medium, or low levels of high school education?  */
/* medium result is not as same as answer */
select
case when sm.msa_high >= 50 and sm.msa_high <= 60 then 'low'
when sm.msa_high >= 60.01 and sm.msa_high <= 70 then 'medium'
when sm.msa_high >= 70 then 'high' end as education,
sum(filter.monthR)/sum(filter.Day_num) as saleamt
from
    store_msa sm join
(
select s.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct extract(day from t.saledate)) as Day_num, sum(amt) as monthR, (monthR/Day_num) as avgdailysale
from trnsact t join strinfo s on t.store = s.store
where t.stype = 'P'
group by s.store, salem, saley
having Day_num >= 20
) as filter
on sm.store = filter.store
group by education


/* Exercise 6. Compare the average daily revenues of the stores with the highest median
msa_income and the lowest median msa_income. In what city and state were these stores,
and which store had a higher average daily revenue? */

select
sm.msa_income, sm.state, sm.city,
sum(filter.monthR)/sum(filter.Day_num) as saleamt
from
store_msa sm join
(
select s.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct extract(day from t.saledate)) as Day_num, sum(amt) as monthR, (monthR/Day_num) as avgdailysale
from trnsact t join strinfo s on t.store = s.store
where t.stype = 'P'
group by s.store, salem, saley
having Day_num >= 20
) as filter
on sm.store = filter.store
group by sm.msa_income, sm.state, sm.city
order by sm.msa_income


/* Exercise 7: What is the brand of the sku with the greatest standard deviation in sprice?
Only examine skus that have been part of over 100 transactions. */

select top 3 s.brand, target.Pstd 
from skuinfo s join (
select sku, stddev_samp(sprice) as Pstd
from trnsact t
having count(amt)>100
group by sku) as target
on s.sku = target.sku
order by target.Pstd desc;

/* Exercise 10: Which department, in which city and state of what store, had the greatest %
increase in average daily sales revenue from November to December?  */

select st.store, st.city, st.state
from strinfo st join
(
    select top 1 t.store, di.dept, sum(case when extract(month from t.saledate) = 12 then t.amt end) as Dec_R,
    count(distinct case when extract(month from t.saledate) = 12 then extract(day from t.saledate) end) as Dec_Day,
    Dec_R/Dec_Day as DecDaily,
    sum(case when extract(month from t.saledate) = 11 then t.amt end) as Nov_R, 
    count(distinct case when extract(month from t.saledate) = 11 then extract(day from t.saledate) end) as Nov_Day,
    Nov_R/Nov_Day as NovDaily,
    ((DecDaily - NovDaily)/NovDaily) * 100 as Pchange
    from trnsact t join skuinfo si on t.sku = si.sku
    join deptinfo di on si.dept = di.dept
    where t.stype = 'P' 
    having Dec_Day >= 20 and Nov_Day >= 20
    group by t.store, di.dept
    order by Pchange desc
) as top1 
on st.store = top1.store;

/* 4. Which sku number had the greatest increase in total sales revenue from November to December? */

select sku, sum(case when extract(month from saledate) = 11 then amt end) as Nov_sale,
sum(case when extract(month from saledate) = 12 then amt end) as Dec_sale,
(Dec_sale - Nov_sale) as increase
from trnsact t join
(select store, extract(month from saledate) as salem, extract(year from saledate) as saley, 
count(distinct extract(day from saledate)) as Day_num
from trnsact 
group by store, saley, salem
having Day_num >=20) as filter
on t.store = filter.store
where t.stype = 'P'
group by sku
order by increase desc;

/*5.  What vendor has the greatest number of distinct skus in the transaction table that do not exist in the skstinfo table? (Remember that vendors are listed as distinct numbers in our data set).*/
select vendor, count(f.sk) as num
from skuinfo s join
(select distinct(t.sku) as sk
from trnsact t left join skstinfo si
on t.sku = si.sku
where t.sku is not null and si.sku is null) f
on s.sku = f.sk
group by vendor
order by num desc;

/* 6. What is the brand of the sku with the greatest standard deviation in sprice? Only examine skus which have been part of over 100 transactions.*/
select s.sku, s.brand, top3.st
from skuinfo s join
(select top 1 sku, stddev_samp(sprice) as st
from trnsact
where stype = 'P'
group by sku
having count(saledate) > 100
order by st desc) as top3
on s.sku = top3.sku

/* 7. What is the city and state of the store which had the greatest increase in average daily revenue (as defined in Teradata Week 5 Exercise Guide) from November to December? */

select st.store, st.city, st.state, top1.Rchange
from strinfo st join
(
    select top 1 t.store, sum(case when extract(month from t.saledate) = 12 then t.amt end) as Dec_R,
    count(distinct case when extract(month from t.saledate) = 12 then extract(day from t.saledate) end) as Dec_Day,
    Dec_R/Dec_Day as DecDaily,
    sum(case when extract(month from t.saledate) = 11 then t.amt end) as Nov_R,
    count(distinct case when extract(month from t.saledate) = 11 then extract(day from t.saledate) end) as Nov_Day,
    Nov_R/Nov_Day as NovDaily,
    DecDaily - NovDaily as Rchange
    from trnsact t join skuinfo si on t.sku = si.sku
    join deptinfo di on si.dept = di.dept
    where t.stype = 'P'
    having Dec_Day >= 20 and Nov_Day >= 20
    group by t.store
    order by Rchange desc
) as top1
on st.store = top1.store;


/* 9. Divide the msa_income groups up so that msa_incomes between 1 and 20,000 are labeled 'low', msa_incomes between 20,001 and 30,000 are labeled 'med-low', msa_incomes between 30,001 and 40,000 are labeled 'med-high', and msa_incomes between 40,001 and 60,000 are labeled 'high'. Which of these groups has the highest average daily revenue (as defined in Teradata Week 5 Exercise Guide) per store? */

select
case when sm.msa_income >=1 and sm.msa_income <=20000 then 'low'
when sm.msa_income >=20001 and sm.msa_income <=30000 then 'med-low'
when sm.msa_income >=30001 and sm.msa_income <=40000 then 'med-high'
when sm.msa_income >=40001 and sm.msa_income <=60000 then 'high'
end as income_level,
sum(filter.monthR)/sum(filter.Day_num) as saleamt
from
store_msa sm join
(
select s.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct extract(day from t.saledate)) as Day_num, sum(amt) as monthR, (monthR/Day_num) as avgdailysale
from trnsact t join strinfo s on t.store = s.store
where t.stype = 'P'
group by s.store, salem, saley
having Day_num >= 20
) as filter
on sm.store = filter.store
group by income_level

/* 11. Which department in which store had the greatest percent increase in average daily sales revenue from November to December, and what city and state was that store located in? Only examine departments whose total sales were at least $1,000 in both November and December. */

select st.store, top1.deptdesc, st.city, st.state
from strinfo st join
(
    select top 1 t.store, di.dept, di.deptdesc, sum(case when extract(month from t.saledate) = 12 then t.amt end) as Dec_R,
    count(distinct case when extract(month from t.saledate) = 12 then extract(day from t.saledate) end) as Dec_Day,
    Dec_R/Dec_Day as DecDaily,
    sum(case when extract(month from t.saledate) = 11 then t.amt end) as Nov_R,
    count(distinct case when extract(month from t.saledate) = 11 then extract(day from t.saledate) end) as Nov_Day,
    Nov_R/Nov_Day as NovDaily,
    ((DecDaily - NovDaily)/NovDaily) * 100 as Pchange
    from trnsact t join skuinfo si on t.sku = si.sku
    join deptinfo di on si.dept = di.dept
    where t.stype = 'P'
    having Dec_Day >= 20 and Nov_Day >= 20 and Nov_R >= 1000 and Dec_R >= 1000
    group by t.store, di.dept, di.deptdesc
    order by Pchange desc
) as top1
on st.store = top1.store;

/* 12. Which department within a particular store had the greatest decrease in average daily sales revenue from August to September, and in what city and state was that store located? */
select st.store, top1.deptdesc, st.city, st.state, top1.rchange
from strinfo st join
(
    select top 1 t.store, di.dept, di.deptdesc, sum(case when extract(month from t.saledate) = 9 then t.amt end) as Sep_R,
    count(distinct case when extract(month from t.saledate) = 9 then extract(day from t.saledate) end) as Sep_Day,
    Sep_R/Sep_Day as SepDaily,
    sum(case when extract(month from t.saledate) = 8 then t.amt end) as Aug_R,
    count(distinct case when extract(month from t.saledate) = 8 then extract(day from t.saledate) end) as Aug_Day,
    Aug_R/Aug_Day as AugDaily,
    AugDaily - SepDaily as Rchange
    from trnsact t join skuinfo si on t.sku = si.sku
    join deptinfo di on si.dept = di.dept
    where t.stype = 'P'and extract(year from t.saledate) <> 2005
    having Sep_Day >= 20 and Aug_Day >= 20 
    group by t.store, di.dept, di.deptdesc
    order by Rchange desc
) as top1
on st.store = top1.store;

/* 13. 
Identify which department, in which city and state of what store, had the greatest DECREASE in the number of items sold from August to September. How many fewer items did that department sell in September compared to August? */

select st.store, top1.deptdesc, st.city, st.state, top1.Qchange
from strinfo st join
(
    select top 1 t.store, di.dept, di.deptdesc, sum(case when extract(month from t.saledate) = 9 then t.quantity end) as Sep_Q,
    count(distinct case when extract(month from t.saledate) = 9 then extract(day from t.saledate) end) as Sep_Day,
    sum(case when extract(month from t.saledate) = 8 then t.quantity end) as Aug_Q,
    count(distinct case when extract(month from t.saledate) = 8 then extract(day from t.saledate) end) as Aug_Day,
    Aug_Q - Sep_Q as Qchange
    from trnsact t join skuinfo si on t.sku = si.sku
    join deptinfo di on si.dept = di.dept
    where t.stype = 'P' and extract(year from t.saledate) <> 2005
    having Sep_Day >= 20 and Aug_Day >= 20 
    group by t.store, di.dept, di.deptdesc
    order by Qchange desc
) as top1
on st.store = top1.store;

/* 14. For each store, determine the month with the minimum average daily revenue (as defined in Teradata Week 5 Exercise Guide) . For each of the twelve months of the year, count how many stores' minimum average daily revenue was in that month. During which month(s) did over 100 stores have their minimum average daily revenue? */
/* use desc and rank_rank = 12: only compare the stores having 12 month data) */

select min_month_sale.salem, count(*) 
from 
(
select t.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct t.saledate) as Day_num, sum(amt) as monthR, (monthR/Day_num) as avgdailysale,
row_number() over (partition by t.store order by avgdailysale desc) as sale_rank
from trnsact t 
where t.stype = 'P' and (saley <> 2005 or salem <> 8)
group by t.store, salem, saley
having Day_num >= 20
qualify sale_rank = 12
) as min_month_sale
group by min_month_sale.salem
order by min_month_sale.salem

/* 15. Write a query that determines the month in which each store had its maximum number of sku units returned. During which month did the greatest number of stores have their maximum number of sku units returned? */

select min_month_sale.salem, count(*) 
from 
(
select t.store, extract(year from t.saledate) as saley, extract(month from t.saledate) as salem,  count(distinct t.saledate) as Day_num, sum(quantity) as monthQ, 
row_number() over (partition by t.store order by avgdailysale) as sale_rank
from trnsact t 
where t.stype = 'R' and (saley <> 2005 or salem <> 8)
group by t.store, salem, saley
having Day_num >= 20
qualify sale_rank = 12
) as min_month_sale
group by min_month_sale.salem
order by min_month_sale.salem
