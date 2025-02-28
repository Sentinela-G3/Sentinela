create user 'sentinelaInsertDados'@'%' identified by 'Sentinela@123';

grant insert on sentinela.processador to 'sentinelaInsertDados'@'%';
grant insert on sentinela.memoria to 'sentinelaInsertDados'@'%';
grant insert on sentinela.bateria to 'sentinelaInsertDados'@'%';
grant insert on sentinela.redeChip to 'sentinelaInsertDados'@'%';
grant insert on sentinela.armazenamento to 'sentinelaInsertDados'@'%';

create user 'sentinelaSelect'@'%' identified by 'Sentinela@123';

grant select on sentinela.* to 'sentinelaSelect'@'%';

create user 'sentinelaInsertCadastro'@'%' identified by 'Sentinela@123';

grant insert on sentinela.usuario to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.endereco to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.empresa to 'sentinelaInsertCadastro'@'%';
grant insert on sentinela.usuarioEndereco to 'sentinelaInsertCadastro'@'%';

flush privileges;