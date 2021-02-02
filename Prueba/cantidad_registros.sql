/*Cantidad de registros
Cree una consulta en SQL que retorne la cantidad de productos por categoría y proveedor que han sido ordenados mes a mes desde el inicio de la compañía.
*/

SELECT B.CategoryName AS CATEGORIA
       ,COUNT(*) AS TOTAL
FROM Products A WITH (NOLOCK)
INNER JOIN Categories B WITH (NOLOCK)
ON A.CategoryID = B.CategoryID
GROUP BY B.CategoryName


