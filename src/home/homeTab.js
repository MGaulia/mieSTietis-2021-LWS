import React from "react";
import HomeCities from "./allcitys/homeCities";
import CityAnimation from "./cityAnimation";
import Alert from "react-bootstrap/Button";
import SelectedCityMain from "./selectedCity/selectedCitymain";
const Home = (props) =>{
    return(
      <div className="" style={{width:"100%", height:"100%", backgroundColor:"rgb(176, 215, 235)", position:"fixed"}}>
      <div className="container" style={{}}>
        <div className="row" style={{marginTop:"20px"}}></div>

        <div className="row">
          {/* cityPanel */}
          <div className="col col-4" style={{backgroundColor:"rgb(233, 236, 239)"}}>
            <SelectedCityMain expand={props.expand} expandCityPanel={props.expandCityPanel} 
            thisCity={props.thisCity} selectCity={props.selectCity}></SelectedCityMain>
          </div>
          {/* Animation and name */}
          <div className="col col-4" style={{backgroundColor:"rgb(233, 236, 239)"}}>
            <CityAnimation expand={props.expand} expandCityPanel={props.expandCityPanel} 
            thisCity={props.thisCity} selectCity={props.selectCity}></CityAnimation>
          </div>
          {/* ALLcitiesPanel */}
          <div className="col col-4" style={{backgroundColor:"rgb(233, 236, 239)"}}>
            <HomeCities thisCity={props.thisCity} selectCity={props.selectCity}></HomeCities>
          </div>
        </div>
      </div>
      
    </div>
    )
}

export default Home