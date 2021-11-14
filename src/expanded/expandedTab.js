import React,{useState} from "react";
import CityAnimationEx from "./cityAnimationEx";
import ExpandedCities from "./allcitys/expandedCities"
import SelectedCityEx from "./selectedCityEx/selectedCityEx";
// ----------------------------------------------- EXPANDED -----------------------------------------------------
const Expanded = (props) => {
  const [hover, setHover] = useState("")
  const seterHover = (value) =>{
    setHover(value)
  }
    return(
      <div className="" style={{width:"100%", height:"100%", backgroundColor:"rgb(176, 215, 235)", position:"fixed"}}>
      <div className="container" style={{}}>
        <div className="row" style={{marginTop:"20px"}}></div>

        <div className="row">
          {/* cityPanel */}
          <div className="col col-8" style={{backgroundColor:"rgb(240, 220, 220)"}}>
            <SelectedCityEx thisCity={props.thisCity} seterHover={seterHover}></SelectedCityEx>
          </div>
          {/* ALLcitiesPanel + animation and name */}
          <div className="col col-4" style={{backgroundColor:"rgb(139, 181, 151)"}}>
            <div className="row">
              <div className="col">
                <div style={{height:"300px", border:"2px solid",borderRadius:"5px", marginTop: "10px", marginBottom:"10px"}}>
                  <div> <ExpandedCities hover={hover}></ExpandedCities></div>
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