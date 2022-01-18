sudo su postgres
postgres@zakka-HP-Pavilion-Gaming-Laptop-15-ec0xxx:/home/zakka$ psql
psql (14.1 (Ubuntu 14.1-2.pgdg20.04+1))
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres

(3 rows)

zakka=# CREATE TABLE playground (
zakka(#     equip_id serial PRIMARY KEY,
zakka(#     type varchar (50) NOT NULL,
zakka(#     color varchar (25) NOT NULL,
zakka(#     location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
zakka(#     install_date date
zakka(# );
CREATE TABLE
zakka=# \d
                  List of relations
 Schema |          Name           |   Type   | Owner 
--------+-------------------------+----------+-------
 public | playground              | table    | zakka
 public | playground_equip_id_seq | sequence | zakka
(2 rows)

                  List of relations
 Schema |          Name           |   Type   | Owner 
--------+-------------------------+----------+-------
 public | hero                    | table    | zakka
 public | hero_equip_id_seq       | sequence | zakka
 public | playground              | table    | zakka
 public | playground_equip_id_seq | sequence | zakka
(4 rows)

zakka=# SELECT * FROM playground;
 equip_id |    type    | color  | location  | install_date 
----------+------------+--------+-----------+--------------
        1 | holahop    | blue   | south     | 2020-01-19
        2 | Bola bekel | yellow | northwest | 2020-01-18
(2 rows)

zakka=# DELETE FROM playground WHERE type = 'holahop';
DELETE 1
zakka=# SELECT * FROM playground;
 equip_id |    type    | color  | location  | install_date 
----------+------------+--------+-----------+--------------
        2 | Bola bekel | yellow | northwest | 2020-01-18
(1 row)

zakka=# UPDATE playground SET color = 'blue' WHERE type = 'Bola bekel';
UPDATE 1
zakka=# SELECT * FROM playground;
 equip_id |    type    | color | location  | install_date 
----------+------------+-------+-----------+--------------
        2 | Bola bekel | blue  | northwest | 2020-01-18
(1 row)

zakka=# UPDATE playground SET location = 'southwest' WHERE type = 'Bola bekel';
UPDATE 1
zakka=# SELECT * FROM playground;
 equip_id |    type    | color | location  | install_date 
----------+------------+-------+-----------+--------------
        2 | Bola bekel | blue  | southwest | 2020-01-18
(1 row)

zakka=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 zakka     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
(4 rows)

zakka=# CREATE TABLE characters (
no serial PRIMARY KEY,
name varchar (50) NOT NULL,
type varchar (50) NOT NULL)
zakka-# ;
CREATE TABLE
zakka=# \d
                   List of relations
 Schema |          Name           |   Type   |  Owner   
--------+-------------------------+----------+----------
 public | characters              | table    | postgres
 public | characters_no_seq       | sequence | postgres
 public | hero                    | table    | zakka
 public | hero_equip_id_seq       | sequence | zakka
 public | playground              | table    | zakka
 public | playground_equip_id_seq | sequence | zakka
(6 rows)

zakka=# INSERT INTO characters (name, type)
zakka-# VALUES ('invoker', 'intelligent');
INSERT 0 1
zakka=# SELECT * FROM characters
;
 no |  name   |    type     
----+---------+-------------
  1 | invoker | intelligent
(1 row)

zakka=# INSERT INTO characters (name, type)
VALUES ('axe', 'strength');
INSERT 0 1
zakka=# INSERT INTO characters (name, type)
VALUES ('juggernaut', 'agility');
INSERT 0 1
zakka=# SELECT * FROM characters
;
 no |    name    |    type     
----+------------+-------------
  1 | invoker    | intelligent
  2 | axe        | strength
  3 | juggernaut | agility
(3 rows)
