# Write your MySQL query statement below
SELECT i.invoice_id,
       c.customer_name,
       i.price,
       COUNT(DISTINCT con.contact_email) AS contacts_cnt,
       COUNT(DISTINCT con_trusted.contact_email) AS trusted_contacts_cnt
FROM Invoices i
JOIN Customers c
     ON i.user_id = c.customer_id
LEFT JOIN Contacts con
     ON i.user_id = con.user_id
LEFT JOIN Contacts con_trusted
     ON i.user_id = con_trusted.user_id
     AND con_trusted.contact_email IN (SELECT email FROM Customers)
GROUP BY i.invoice_id, c.customer_name, i.price
ORDER BY i.invoice_id;
