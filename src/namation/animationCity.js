import React,{useState} from "react";
import alytusHerb from "../Alytus.png";
import klaipedaHerb from "../Klaipėda.png";
import vilniusHerb from "../Vilnius.png";
import siauliaiHerb from "../Šiauliai.png";
import panevezysHerb from "../Panevėžys.png";
import kaunasHerb  from "../Kaunas.png";
import ExpandButton from "./expandButton";



const AnimationCity = (props) => {
    const [city, setCity] = useState(props.thisCity)
    const miestai = ["Vilnius","Kaunas","Klaipėda","Šiauliai","Panevėžys","Alytus"]
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
    const herbas = () => {
        switch (true) {
            case (props.thisCity === "Alytus"):
                return(
                    <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                    <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={alytusHerb} alt="Logo" />
                    </div>
                )
                
                
                break;
                case (props.thisCity === "Kaunas"):
                    return(
                    <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                        <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={kaunasHerb} alt="Logo" />
                    </div>)
                    
                    break;
                case (props.thisCity === "Vilnius"):
                    return(
                <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                    <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={vilniusHerb} alt="Logo" />
                </div>)
                
                break;
                case (props.thisCity === "Klaipėda"):
                    return(
                <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                    <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={klaipedaHerb} alt="Logo" />
                </div>)
                
                break;
                case (props.thisCity === "Šiauliai"):
                    return(
                <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={siauliaiHerb} alt="Logo" />
                </div>)
                
                break;
                case (props.thisCity === "Panevėžys"):
                    return(
                <div style={{height: "200px", width:"100%",display:"flex", justifyContent:"center" }}>
                <img style={{height: "200px", marginRight:"auto", marginLeft:"auto"}} src={panevezysHerb} alt="Logo" />
                </div>)
                
                break;
        
            default:
                break;
        }
    }
    return(
        <div style={{position:"absolute", zIndex:"10"}}>
            <div style={{position:"absolute", zIndex:"10", marginTop:"150px", }}>
                <ExpandButton expand={props.expand} expandCityPanel={props.expandCityPanel}></ExpandButton>
            </div>
            
            <div style={{width:"400px",position:"absolute", display:"flex", justifyContent:"space-between", marginTop:"400px"}}>
            <div  onClick={()=> arrowL()}>
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-arrow-left-square" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
</svg>
            </div>
            <div onClick={()=> arrowR()}>
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-arrow-right-square" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm4.5 5.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
</svg>
            </div>
            </div>
            
            {/* miesto pavadinimas */}
            <div style={{position:"absolute", zIndex:"10", marginTop:"300px", marginLeft:"120px"}}>
            <div style={{width:"100%", textAlign:"center",fontSize:"30px"}}>
                {city}
            </div>
            {/* vizualizacija */}
            {herbas()}
            </div>
        </div>
    )
}

export default AnimationCity