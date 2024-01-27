# Запрос 1
SELECT "Couriers".login,
        COUNT(*)
FROM "Couriers"
INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;

# Запрос 2
SELECT "Orders"."track",
   CASE
     WHEN "Orders"."finished" = true THEN 2
     WHEN "Orders"."cancelled" = true THEN -1
     WHEN "Orders"."inDelivery" = true THEN 1
   ELSE 0
END AS status
FROM "Orders"
INNER JOIN "Couriers" ON "Couriers".id = "Orders"."courierId";


