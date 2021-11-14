import React, { useEffect,useState } from "react";

const HomeCities = () =>{
    const [data, setData] = useState(null)
    useEffect(() => {
        
    },[])
    const dividerStyle = {borderTop:"3px solid", borderRadius:"5px", borderColor:"rgb(124, 128, 126)",
    margin:"0px 10px 0px 10px", marginLeft:"10px", marginRight:"10px"}
    return(
    <div style={{height:"670px", border:"2px solid",borderRadius:"5px", marginTop: "10px", marginBottom:"10px",
    display:"flex",flexDirection: "column"}}>
        <div style={{paddingLeft:"10px",fontSize:"30px"}}>Visi Miestai</div>
            <hr className="" style={dividerStyle}></hr>
    </div>)
}

export default HomeCities