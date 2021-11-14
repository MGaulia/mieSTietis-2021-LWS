import React,{useEffect, useState} from "react";
import Alert from "react-bootstrap/Alert";

import "./App.css"
import { Line } from 'react-chartjs-2';

const Test = (props) => {
  const [data, setData] = useState({"x":[],"y":[]})
    useEffect(() => {
        fetch(
            "http://127.0.0.1:5000/nuotekos")
                        .then((res) => res.json())
                        .then((json) => {
                          let miestas = props.thisCity
                          setData(json[miestas])
                          console.log(json[miestas])
                        })
  },[props.thisCity])
  const showingData = {
    labels: data.x,
    datasets: [
      {
        label: '# of Votes',
        data: data.y,
        fill: false,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgba(255, 99, 132, 0.2)',
        borderWidth: '6',
      },
    ],
  };
  const options = {
    scales: {
      y: {
        beginAtZero: false
      }
    }
  };

  console.log(data)
  
  

  return(
  <>
    <Line data={showingData} options={options} />
  </>
);
}
export default Test;