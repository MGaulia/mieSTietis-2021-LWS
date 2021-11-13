import React,{useState} from 'react';
import './App.css';
import Button from "react-bootstrap/Button"
import Alert from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css"
import Test from "./test"

import Home from './home/homeTab';
import Expanded from './expanded/expandedTab';


function App() {
  const [expand, setExpand] = useState(false)
  const [city, setCity] = useState("Vilnius")
  
  const expandCityPanel = () => {
    setExpand(!expand)
  }
  const selectCity = (thisCity) => {
    setCity(thisCity)
  }

  // ----------------------------------------------- HOME -----------------------------------------------------
  
  
  return (
    <div>{expand?
    <Expanded
    expand={expand} expandCityPanel={expandCityPanel}
                thisCity={city} selectCity={selectCity}/>:
    <Home
    expand={expand} expandCityPanel={expandCityPanel}
                thisCity={city} selectCity={selectCity}/>}</div>
  );
}

export default App;
