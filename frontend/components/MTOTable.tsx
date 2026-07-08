export default function MTOTable({items}:any){

if(!items) return null;


return (

<table border={1}>

<thead>

<tr>

<th>No</th>
<th>Category</th>
<th>Description</th>
<th>Size</th>
<th>Qty</th>
<th>Unit</th>

</tr>

</thead>


<tbody>

{items.map((x:any)=>(

<tr key={x.item_no}>

<td>{x.item_no}</td>

<td>{x.category}</td>

<td>{x.description}</td>

<td>{x.size_nps}</td>

<td>{x.quantity}</td>

<td>{x.unit}</td>


</tr>


))}

</tbody>

</table>

)

}