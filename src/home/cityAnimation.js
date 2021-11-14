import React, {useState} from "react";
import ExpandButton from "../namation/expandButton";
import AnimationCity from "../namation/animationCity";
import backr from "../download.png"
const CityAnimation = (props) => {


    return(
    <div style={{height:"670px",  marginTop: "10px", marginBottom:"10px", display:"flex",flexDirection: "column", zIndex:"20"}}>
        
        {/* Grafiko pavadinimas */}
        <div className="" style={{textAlign: "center", fontSize:"30px"}}>Pradėkime nuo savo miesto</div>
        {/* sub pavadinimas */}
        <div className="" style={{textAlign: "center", fontSize:"15px"}}>Ekologinių miestų rodiklių vizualizacija</div>
        
        {/* <div style={{marginTop:"50px", backgroundImage:'"../download.png"', display:"flex", flexDirection:"column",
        backgroundSize:"440px 500px", opacity:"0.2"
    }}> */}
        <div>
            
            <div>
                <AnimationCity thisCity={props.thisCity} selectCity={props.selectCity}
                expand={props.expand} expandCityPanel={props.expandCityPanel}></AnimationCity>
            </div>
            
        </div>
        {/* <div style={{position:"absolute", opacity:"0.2", marginTop:"200px", zIndex:"0"}}>
            <img src={backr} style={{width:"400px"}}></img>
        </div> */}
        <div style={{position:"relative", opacity:"0.2", marginTop:"200px", zIndex:"0"}}>
            <img src={backr} style={{width:"400px"}}></img>
        </div>
        
        

    </div>
    )
}

export default CityAnimation