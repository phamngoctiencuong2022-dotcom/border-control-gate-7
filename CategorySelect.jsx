"use client"
import { getCategories } from '@/services/categoryService';
import React, { useEffect, useState } from 'react'
import Select from './Select';
export default function CategorySelect() {
const [categories, setCategories] = useState([]);
const [loading, setLoading] = useState(true);
const [errors, setError] = useState({});
// goi api
useEffect(() => {
const fetchData = async () => {
try {
setLoading(true);
const data = await getCategories({ trash: 0 });
setCategories(data);
}
catch (e) {
setErrors(e.data.error);
}
finally {
setLoading(false);
}
};
fetchData();
}, [])
console.log(categories);
return (
<div>
{isEmpty(errors) ? <p> {error.message}</p> : loading ?
"loading categories" : <Select options={categories} valueKey="cat_id" labelKey="cat_name" />}
</div>
)
}