
-- self join:-

use RevCompanyDb;

select * from emp;

select e.ename as "Employee",m.ename as "Manager"
from emp e join emp m
on e.mgr=m.empno;

select e.ename as "Employee Name",d.dname as "Dname"
from emp e cross join dept d;

-- Subquery

-- It will return the where the depno is equal to subquery where dname ia deptno
select ename from emp 
where deptno=(select deptno
from dept
where dname='sal'
)

select ename from emp 
where deptno=(select deptno
from dept
where dname='qc'
)

-- Name the employee who are getting more salary than average
select ename,sal from emp
where sal>(select avg(sal) from emp);

-- Second highest salary
select max(sal) from emp 
where sal<(select max(sal) from emp)

-- Dept wise avgrage salary

select deptno,avg(sal) from emp 
group by deptno;

select ename,sal from emp
where
sal>(select avg(sal) from emp);


select max(sal) from emp 
where
sal<(select max(sal) from emp)



select e.ename,d.dname from emp e
inner join dept d 
on d.deptno=e.deptno

-- view-->virtual table which not any store 
create view vemp as select empno,ename from emp where deptno in (10,20,30);

select * from vemp;


/*
Index:-An index in SQL is a special data structure that improves 
the speed of data retrieval operations by allowing the database 
to quickly locate rows without scanning the entire table.

Syntax:-CREATE INDEX idx_empname ON emp(ename);
*/

/*
Clutstered Index:- Sorts and stored the data rows in the table based on the key.
only one per table
Non-Clusterd Index:-
*/

create nonclustered  index indeptno on emp(deptno);


/*
Procedure in mysql:-It is a block of code which that perform the specific task and 
can be use multiple times

Syntax:-
create or alter procedure name
@varible name int,@name varchar 
as
begin
    you logic
end

for run 
exec procdeure_Name varble_value,name
*/

create or alter procedure sp_empdate
@empno int,@ename varchar(30),@deptno int,@sal numeric(10,2)
as
begin
   begin transaction
      insert into emp(empno,ename,deptno,sal) values(@empno,@ename,@deptno,@sal)
      update emp set comm=sal*0.1 where empno=@empno
      commit;
      select * from emp;
      return 1
end

declare @status int;
exec @status = sp_empdate 1013,'Sunil',20,55000.00;
print @status;

select * from emp
delete from emp where empno=1012


/* Function :-
   it is a block of code which take a paramter as input and perform single operation and
   return the single value.
   It’s used to encapsulate logic for calculations, formatting, or data transformation.
*/ 

-- This is Scalar Function which return the single values
create or alter function  dbo.EmpInsertion(@empno int,@ename varchar)
returns varchar(20)
as
begin
    return cast(@empno as varchar) +'-'+@ename
end

select dbo.EmpInsertion(2002,'raman') response -->It return the single value so * is not required

-- 
create or alter function AvgSal()
returns table
as
  return(
      select deptno,avg(sal) as "Avg Salary" from emp group by deptno
  );

select * from AvgSal() response --It return the Whole table so treat like table so * is required
/*
SQL Server Interview Prep: Function vs Procedure
🔹 1. Definition
- Function: A reusable block that returns a value. Used in SELECT, WHERE, etc.
- Procedure: A block that performs actions (like insert/update) and may return a value.

🔹 2. Key Differences
- Return Type:
- Function: Must return a value
- Procedure: Optional return (can use RETURN, OUTPUT, PRINT)
- Data Modification (INSERT/UPDATE/DELETE):
- Function: ❌ Not allowed
- Procedure: ✅ Allowed
- Usage in SELECT:
- Function: ✅ Yes
- Procedure: ❌ No
- Transactions (BEGIN TRAN):
- Function: ❌ Not allowed
- Procedure: ✅ Allowed
- Error Handling (TRY...CATCH):
- Function: ❌ Not allowed
- Procedure: ✅ Allowed
- Deterministic Requirement:
- Function: ✅ Must be deterministic
- Procedure: ❌ Not required

*/
-- A schema is a logical container for database objects like tables, views,
-- procedures, and functions.

/* 
 When we do contadiction of number and string it will shows error for that
 we can use {CAST} for converting int to string
*/



/*  
Triggers:-A trigger is a special kind of stored procedure that automatically 
executes in response to certain events on a table or view.
-Think of it like a "reaction" — when something happens (like an insert, update, or delete),
 the trigger fires and performs predefined logic

 Syntax:-
 CREATE TRIGGER trg_AuditInsert
ON emp
AFTER INSERT/Before insert
AS
BEGIN
    INSERT INTO emp_audit(empno, action, action_time)
    SELECT empno, 'INSERT', GETDATE()
    FROM inserted;
END;
*/

-- After trigger 
create trigger trg_afterInsertEmp
on emp
after insert
as
begin 
     print 'new employee recorde inserted into emp table.';
end

insert into emp (empno,ename) values (1112,'ABC');

