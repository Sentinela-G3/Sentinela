create user 'sentinelaInsert'@'%' identified by 'Sentinela@123';

grant insert on sentinela.* to 'sentinelaInsert'@'%';

create user 'sentinelaSelect'@'%' identified by 'Sentinela@123';

grant select on sentinela.* to 'sentinelaSelect'@'%';

flush privileges;