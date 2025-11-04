use KVCERTDB;

/*
Transaction is the one or more  set of operation that are operate as a 
single unit
with the help of transcation does the command will be 
execute or either fails
*/
begin transaction;

insert into student(studId,sname,marks,age,city,pin) 
values (101,'Raman',85,24,'Latur',413512), 
(102,'Raj',93,22,'Parbhani',413518), 
(103,'Sunil',80,26,'Pune',410502), 
(104,'Dipak',88,23,'Nanaded',413512); 

insert into dbo.student values(105,'Rushi',88,23,'Dharashiv',413512);

select * from student;

-- Save cretae a savepoint to undo
save transaction level1;
insert into dbo.student values(106,'Ashish',75,23,'Sangali',411512);
save transaction level2;
 
update student set city='Latur'
where studId=103;
-- rollback:-It undo the changes that recently done
rollback transaction level2;

-- Commit :-It save all changes permantly
commit transaction;

delete student where studId=104;

truncate table student;


create database RevCompanyDb;
use RevCompanyDb;

create table dept(
deptno smallint,
dname varchar(20) not null,
constraint pl_deptno primary key(deptno)
);

create table emp(empno smallint ,
ename varchar(30) not null ,
mgr smallint,
sal numeric(10,2),
comm numeric(7,2),
deptno smallint,
constraint pk_empno primary key(empno),
constraint fk_deptno foreign key(deptno) references dept(deptno)
)

insert into dept values(10,'IT')
insert into dept values(20,'HR')
insert into dept values(30,'SAL')
insert into dept values(40,'MKt')
insert into dept values(50,'OPS')

-- valid inserts (deptno 20 and 30 exist)
INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10),  -- HR
(1002, 'Bob', 1001, 75000.00, NULL, 20),    -- IT
(1003, 'Charlie', 1002, 50000.00, 500.00, 30), -- Sales
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   -- Sales
(1005, 'Ethan', 1002, 58000.00, NULL, 40),  -- Finance
(1006, 'Fiona', 1005, 62000.00, NULL, 50);  -- Marketing


select * from dept;
select * from emp;

-- it will select only ename and eno fecth data in that column
select empno as 'emp_id', ename as "name" from emp; 

-- it will retrival salary greater than 50000 in desc order by sal
select empno,ename,sal from emp 
where sal>50000
order by sal desc;

-- It will retrival in desc order by sal and commision
select empno,ename,sal,comm from emp 
order by comm,sal desc;


-- Aggreagate Functions
-- It will retrivue the no of employee whose salary is greater than 50000
select count(empno) as 'No of Employee' from emp
where sal>50000;

--Find total salary,maximum,minimum,avg of commition
select sum(sal) as 'total',max(sal) as'Maximum',min(sal) as 'Minimum Salary',
avg(comm) as 'Average commition' 
from emp


-- It will return the value of total salary to each dept no 
select deptno as "Dept number",sum(sal) as "Total_Salary"
from emp
group by deptno;

-- 
select deptno as "Department" ,count(empno) as "Total employee" from emp
group by deptno;


-- It will return the sum of salary within the depno of each below mention
select deptno as "Department",sum(sal) as "Total salary"
from emp 
group by deptno
having deptno in(10,30,40);

-- We can use  the where also these is more efficient than having
select deptno as "Department",sum(sal) as "Total salary"
from emp 
where deptno in(10,30,40)
group by deptno;

-- It will return the total salary greater than 100000
select deptno as "Department",sum(sal) as "Total salary"
from emp 
group by deptno
having  sum(sal)>100000;

select deptno as "Department",sum(sal) as "Total salary"
from emp 
where deptno in(10,30,40)
group by deptno
having  sum(sal)>=62000
order by sum(sal);

insert into dept values
(60,'QC'),
(70,'CC')

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1007, 'Raman', NULL, 60000.00, NULL, null),   
(1008, 'Ashish', 1001, 75000.00, NULL, null),    
(1009, 'Raj', 1002, 50000.00, 500.00, null);

-- Join
-- Inner join return the both Matched value from both table
select e.ename,d.dname from emp e
inner join 
dept d on e.deptno=d.deptno;

--Left join:-Return whole Data left table and from right table only matched value
select e.ename,d.dname from emp e
left join
dept d on e.deptno=d.deptno

--Right join:-Return whole Data Right table and from left table only matched value
select e.ename,d.dname from emp e
right join
dept d on e.deptno=d.deptno

--Outer join :-It will return the both table from left and right
select e.ename,d.dname from emp e
left join
dept d on e.deptno=d.deptno
union
select e.ename,d.dname from emp e
right join
dept d on e.deptno=d.deptno