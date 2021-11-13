import React from "react";
import CityAnimationEx from "./cityAnimationEx";
import ExpandedCities from "./allcitys/expandedCities"
// ----------------------------------------------- EXPANDED -----------------------------------------------------
const Expanded = (props) => {
    return(
      <div className="" style={{width:"100%", height:"100%", backgroundColor:"rgb(176, 215, 235)", position:"fixed"}}>
      <div className="container" style={{}}>
        <div className="row" style={{marginTop:"20px"}}></div>

        <div className="row">
          {/* cityPanel */}
          <div className="col col-8" style={{backgroundColor:"rgb(144, 209, 178)"}}>
            <div style={{height:"600px", border:"2px solid",borderRadius:"5px", marginTop: "10px", marginBottom:"10px"}}>
              <div> Vilnius</div>
            </div>
          </div>
          {/* ALLcitiesPanel + animation and name */}
          <div className="col col-4" style={{backgroundColor:"rgb(139, 181, 151)"}}>
            <div className="row">
              <div className="col">
                <div style={{height:"300px", border:"2px solid",borderRadius:"5px", marginTop: "10px", marginBottom:"10px"}}>
                  <div> <ExpandedCities></ExpandedCities></div>
                </div>
              </div>
            </div>

            <div className="row">
              <div className="col">
                <CityAnimationEx expand={props.expand} expandCityPanel={props.expandCityPanel}
                thisCity={props.thisCity} selectCity={props.selectCity}></CityAnimationEx>
              </div>
            </div>

          </div>
        </div>
      </div>
      
    </div>
    )
  }

export default Expanded