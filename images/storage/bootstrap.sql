-- default settings for all db

create user kobe with encrypted password 'bryant';
create database mediatry template DEFAULT;
grant all privileges on database mediatry to kobe;

