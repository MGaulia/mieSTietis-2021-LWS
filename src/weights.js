import React, {useEffect, useState} from "react"
import Button from "react-bootstrap/esm/Button"

const Weights =(props) =>{
    const [vanduo, setVanduo] = useState()
    const [siuksles, setSiuksles] = useState()
    const [oras, setOras] = useState()
    const [trans, setTrans] = useState()
    
    
    const find = () =>{
        let value = trans + vanduo + oras + siuksles
        fetch("http://127.0.0.1:5000/uw", {
            method: "POST",
            headers: {
                        
                        "Content-Length":0,
                        "Accept":"*/*",
                        "Accept-Encoding":"gzip, deflate, br",
                        "Connection":"keep-alive",
                        "mode": 'no-cors',

                    },
            body: JSON.stringify({text:value})
          }).then(res => {
            console.log("Request complete! response:", res);
          });
    }
    const style1 = {width:"40px", marginRight:"10px"}
    return(
        <div style={{width:"400px", backgroundColor:""}}>
            <div >
                <input style={style1} onChange={(x) => setVanduo(x.target.value)}>

                </input>
                <input style={style1} onChange={(x) => setOras(x.target.value)}>

                </input>
                <input style={style1} onChange={(x) => setTrans(x.target.value)}>

                </input>
                <input style={style1} onChange={(x) => setSiuksles(x.target.value)}>

                </input>
                
                <Button style={{color:"black", backgroundColor:"white", borderColor:"black"}} onClick={() =>find()}> Keisti svorius</Button>
            </div>
        </div>
    )
}

export default Weights