import React, {useState} from "react"
import Button from "react-bootstrap/esm/Button"

const weights =(props) =>{
    const [input,setInput] = useState(null)
    const [free, setFree] = useState(true)

    const find = () =>{
        props.inputing(input, free)
    }

    return(
        <div style={{width:"200px", backgroundColor:"white"}}>
            <div >
            <input onChange={(x) => setInput(x.target.value)}>
            </input>
            <Button onClick={() =>find()}> Search</Button>
            <Button style={{marginLeft:"20px"}}onClick={() => setFree(!free)}>{free? "show last":"show first"}</Button>
            </div>
        </div>
    )
}