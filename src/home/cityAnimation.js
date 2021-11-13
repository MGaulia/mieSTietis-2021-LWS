import React, {useState} from "react";
import ExpandButton from "../namation/expandButton";
import AnimationCity from "../namation/animationCity";
const CityAnimation = (props) => {


    return(
    <div style={{height:"600px",  marginTop: "10px", marginBottom:"10px", display:"flex",flexDirection: "column"}}>
        <div style={{position:"absolute", marginTop:"275px"}}>
            <ExpandButton expand={props.expand} expandCityPanel={props.expandCityPanel}></ExpandButton>
        </div>
        {/* Grafiko pavadinimas */}
        <div className="" style={{textAlign: "center", fontSize:"30px"}}>Pradėkime nuo savo miesto</div>
        {/* sub pavadinimas */}
        <div className="" style={{textAlign: "center", fontSize:"15px"}}>Ekologinių miestų rodiklių vizualizacija</div>
        <div style={{marginTop:"auto"}}>
            <AnimationCity thisCity={props.thisCity} selectCity={props.selectCity}></AnimationCity>
        </div>
        
        

    </div>
    )
}

export default CityAnimation