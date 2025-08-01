INSERT INTO "Employees" (id_employee, first_name, last_name, cnp, email, id_manager)
SELECT
  'A' || LPAD((100 + gs)::text, 3, '0') AS id_employee,
  CASE gs
    WHEN 1 THEN 'Manea'
    WHEN 2 THEN 'Azoitei'
    ELSE 'Angajat_' || gs
  END AS first_name,
  CASE gs
    WHEN 1 THEN 'Matei'
    WHEN 2 THEN 'Paul'
    ELSE 'Test_' || gs
  END AS last_name,
  (FLOOR(RANDOM()*9000000000000 + 1000000000000))::BIGINT::TEXT AS cnp,
  LOWER(
    CASE gs
      WHEN 1 THEN 'manea.matei'
      WHEN 2 THEN 'paul.azoitei'
      ELSE 'angajat_' || gs || '.test_' || gs
    END || '@SolarNyx.com'
  ) AS email,

  ('M10' || (1 + FLOOR(RANDOM()*2))::INT)::TEXT AS id_manager
FROM generate_series(1, 5) AS gs;

INSERT INTO "Employees" (id_employee, first_name, last_name, cnp, email, id_manager)
SELECT
  'M10' || gs AS id_employee,
  CASE gs
    WHEN 1 THEN 'Popescu'
    WHEN 2 THEN 'Georgescu'
    ELSE 'Manager_' || gs
  END AS first_name,
  CASE gs
    WHEN 1 THEN 'Andrei'
    WHEN 2 THEN 'Ioana'
    ELSE 'Test_' || gs
  END AS last_name,
  (FLOOR(RANDOM()*9000000000000 + 1000000000000))::BIGINT::TEXT AS cnp,
  LOWER(
    CASE gs
      WHEN 1 THEN 'andrei.popescu'
      WHEN 2 THEN 'ioana.georgescu'
      ELSE 'manager_' || gs || '.test_' || gs
    END || '@example.com'
  ) AS email,
  NULL AS id_manager
FROM generate_series(1, 2) AS gs;

INSERT INTO "Salaries" (id_employee, base_salary, month)
SELECT
  e.id_employee,
  FLOOR(RANDOM() * 5000 + 3000)::INT,
  TO_CHAR(CURRENT_DATE, 'YYYY-MM')
FROM "Employees" e;


INSERT INTO "Attendance" (
  id_employee, hours_worked, hours_overtime, hours_weekend, hours_holiday, day_vacation, month
)
SELECT
  e.id_employee,
  FLOOR(RANDOM()*40 + 140)::INT,
  FLOOR(RANDOM()*20)::INT,
  FLOOR(RANDOM()*10)::INT,
  FLOOR(RANDOM()*8)::INT,
  FLOOR(RANDOM()*5)::INT,
  DATE_TRUNC('month', CURRENT_DATE)::DATE
FROM "Employees" e;

INSERT INTO "Bonus" (id_employee, apply_bonus_overtime, apply_bonus_weekend, apply_bonus_holiday)
SELECT
  e.id_employee,
  (RANDOM() < 0.5),
  (RANDOM() < 0.5),
  (RANDOM() < 0.5)
FROM "Employees" e;

select * from "Employees"
select * from "Attendance"
select * from "Bonus"
select * from "Salaries"

delete from "Employees";
delete from "Attendance";
delete from "Bonus";
delete from "Salaries";

update "Employees" set email='paul.azoitei@endava.com' where id_employee='A102';
update "Employees" set email='matei.manea@endava.com' where id_employee='A101';
update "Employees" set email='maria.secrieru@endava.com@endava.com' where id_employee='A103';
update "Employees" set email='victor.rosca@endava.com' where id_employee='A104';
update "Employees" set email='alina.brinza@endava.com' where id_employee='M101';
update "Employees" set first_name='Ramfu',last_name='Alina' where id_employee='M101';
update "Employees" set first_name='Rosca',last_name='Victor' where id_employee='A104';
update "Employees" set first_name='Secrieru',last_name='Elisa' where id_employee='A103';