import React, { useEffect,useState } from "react";
import { Line } from "react-chartjs-2";
const ExpandedCities = (props) =>{
    const [data, setData] = useState(null)
    useEffect(() => {
        fetch(
            "http://127.0.0.1:5000/nuotekos")
                        .then((res) => res.json())
                        .then((json) => {
                            setData(json)
                        })
    },[props.hover])
    console.log(data)
    return(
    <div>
        {props.hover}
        <AllKPI></AllKPI>
    </div>)
}
const AllKPI = () =>{
    const [data, setData] = useState(null)
    const [datasets, setDatasets] = useState(null)

    useEffect(() => {
        fetch(
            "http://127.0.0.1:5000/nuotekos")
                        .then((res) => res.json())
                        .then((json) => {
                            setData(json)
                            let dataset = []
                            Object.keys(json).forEach(key => {
                                dataset.push({
                                    label: '# of Votes',
                                    data: json[key].x,
                                    fill: false,
                                    backgroundColor: 'rgb(255, 99, 132)',
                                    borderColor: 'rgba(255, 99, 132, 0.2)',
                                })
                              });
                            setDatasets(dataset)
                            
                        })
    },[])

    
    const options ={

    }
    return(
        <div>
            {(datasets!==null)?<Line data={{
        labels: data.Vilnius.x,
        datasets: datasets,
    }} options={options} />:null}
        </div>
    )

}
export default ExpandedCities