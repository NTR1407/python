/*Consulta de proveedores
Cree una consulta en SQL que retorne cuales han sido las compañías proveedoras de los productos contenidos en todo el historial de ordenes de un cliente en específico, organice alfabéticamente los resultados. 
Customer ID = a
*/


SELECT D.CompanyName
FROM Orders A WITH (NOLOCK)
INNER JOIN [Order Details] B WITH (NOLOCK)
ON A.OrderID = B.OrderID
INNER JOIN Products C WITH (NOLOCK)
ON B.ProductID = C.ProductID
INNER JOIN Suppliers D WITH (NOLOCK)
ON C.SupplierID = D.SupplierID
WHERE A.[Customer ID] = 'a'
    