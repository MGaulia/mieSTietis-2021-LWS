import React,{useState} from "react"

const AnimationCity = (props) => {
    const [city, setCity] = useState(props.thisCity)
    const miestai = ["Vilnius","Kaunas","Klaipėda","Šauliai","Panevėžys","Alytus"]
    console.log(city)
    const arrowR = () => {
        let index = miestai.indexOf(city)
        if(index === miestai.length-1){
            index = 0
        }else{
            index = index+1
        }
        setCity(miestai[index])
        props.selectCity(miestai[index])
    }
    const arrowL = () => {
        let index = miestai.indexOf(city)
        if(index === 0){
            index = miestai.length - 1
        }else{
            index = index -1
        }
        setCity(miestai[index])
        props.selectCity(miestai[index])
    }
    return(
        <div>
            <div style={{width:"400px",position:"absolute", display:"flex", justifyContent:"space-between", }}>
            <div  onClick={()=> arrowL()}>
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-arrow-down-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M2 13.5a.5.5 0 0 0 .5.5h6a.5.5 0 0 0 0-1H3.707L13.854 2.854a.5.5 0 0 0-.708-.708L3 12.293V7.5a.5.5 0 0 0-1 0v6z"/>
                </svg>
            </div>
            <div onClick={()=> arrowR()}>
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-arrow-down-right" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M14 13.5a.5.5 0 0 1-.5.5h-6a.5.5 0 0 1 0-1h4.793L2.146 2.854a.5.5 0 1 1 .708-.708L13 12.293V7.5a.5.5 0 0 1 1 0v6z"/>
                </svg>
            </div>
            </div>
            
            {/* miesto pavadinimas */}
            <div style={{width:"100%", textAlign:"center",fontSize:"30px"}}>
                {city}
            </div>
            {/* vizualizacija */}
            <div style={{height: "200px", width:"100%"}}>

            </div>
        </div>
    )
}

export default AnimationCity