import React, { useEffect,useState } from "react";

const ExpandedCities = () =>{
    const [data, setData] = useState(null)
    useEffect(() => {
        fetch(
            "http://127.0.0.1:5000/nuotekos")
                        .then((res) => res.json())
                        .then((json) => {
                            setData(json)
                        })
    },[])
    console.log(data)
    return(
    <div>
        visi miestai
    </div>)
}
export default ExpandedCities