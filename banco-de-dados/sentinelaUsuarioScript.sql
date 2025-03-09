create user 'sentinelaInsertDados'@'%' identified by 'Sentinela@123';

grant insert on sentinela.dados to 'sentinelaInsertDados'@'%';

create user 'sentinelaSelect'@'%' identified by 'Sentinela@123';

grant select on sentinela.* to 'sentinelaSelect'@'%';

create user 'sentinelaInsertCadastro'@'%' identified by 'Sentinela@123';

grant insert on sentinela.usuario to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.endereco to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.empresa to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.usuarioEndereco to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.maquina to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.componente to 'sentinelaInsertCadastro'@'%';

create user 'sentinelaTestes'@'%' identified by 'Sentinela@123';

grant all on sentinela.* to 'sentinelaTestes'@'%';

flush privileges;