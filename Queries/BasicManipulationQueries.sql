-- selecting databse
use Test_DB;

-- creating table
create table vendor (vendorID varchar(10) primary key not null, firstName varchar(20), lastName varchar(20), phoneNumber int(10), email varchar(30) not null);

-- inserting values to table
insert into vendor values ('V0001', 'Lakshay', 'Saini', '123456789', 'test@example.com');

-- For getting all the available tabes in selected database
show tables;

-- For getting structure of database 
describe vendor;

-- for displaying table content
select * from vendor;

-- alter table
alter table vendor modify column phoneNumber int(15);

-- delete row
delete from vendor where vendorID=''
 