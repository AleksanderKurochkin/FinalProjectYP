# FinalProjectYP

Проект из двух частей

  1 часть: запросы в БД

        1 запрос:
          SELECT c.login, COUNT(o.id) AS "deliveryCount" 
          FROM "Couriers" AS c 
          LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
          WHERE o."inDelivery" = true 
          GROUP BY c.login;

       2 запрос:
           SELECT track, 
              CASE 
	        WHEN finished = true THEN 2 
	        WHEN cancelled = true THEN -1 
	        WHEN "inDelivery" = true THEN 1 
	  ELSE 0 END AS status 
          FROM "Orders";
  Для данных запросов приложены скиншоты.

2 часть: автоматизация теста.

Для запуска теста необходимо в файл configuration скопировить актуальный URL
В файле sendor_stand_request нажать кнопку Run 
        
