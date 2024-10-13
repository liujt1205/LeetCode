# Write your MySQL query statement below
SELECT i.invoice_id,
       c.customer_name,
       i.price,
       COUNT(DISTINCT con.contact_email) AS contacts_cnt,
       COUNT(DISTINCT c_trusted.customer_name) AS trusted_contacts_cnt
FROM Invoices i
JOIN Customers c
     ON i.user_id = c.customer_id
LEFT JOIN Contacts con
     ON i.user_id = con.user_id
LEFT JOIN Customers c_trusted
     ON con.contact_email = c_trusted.email
GROUP BY i.invoice_id, c.customer_name, i.price
ORDER BY i.invoice_id;
