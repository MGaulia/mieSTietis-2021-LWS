import React from "react";
import ExpandButton from "../namation/expandButton";
import AnimationCity from "../namation/animationCity";
import AnimationCityEx from "../namation/animatiopnCityEx";
import backr from "../download.png"

const CityAnimationEx = (props) => {
    return(
        <div style={{height:"300px",  marginTop: "10px", marginBottom:"10px", display:"flex",flexDirection: "column"}}>
        <div style={{position:"absolute", zIndex:"10"}}>
            <ExpandButton expand={props.expand} expandCityPanel={props.expandCityPanel}></ExpandButton>
        </div>
        {/* Grafiko pavadinimas */}
        {props.expand?null:<div><div className="" style={{textAlign: "center", fontSize:"30px"}}>Pradėkime nuo savo miesto</div>
        <div className="" style={{textAlign: "center", fontSize:"15px"}}>Ekologinių miestų rodiklių vizualizacija</div></div>
        }
        {/* sub pavadinimas */}
        <div style={{marginTop:""}}>
            <AnimationCityEx thisCity={props.thisCity} selectCity={props.selectCity}></AnimationCityEx>
        </div>

        <div style={{position:"relative", opacity:"0.2", marginTop:"0", zIndex:"0"}}>
            <img src={backr} style={{width:"400px", height:"350px"}}></img>
        </div>
    </div>

    )
}
export default CityAnimationEx