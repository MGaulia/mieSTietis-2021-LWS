import React, { useEffect,useState } from "react";
import { Line } from "react-chartjs-2";
const ExpandedCities = (props) =>{
    const [data, setData] = useState(null)
    const [render, setRender] = useState(null)
    useEffect(() => {
        switch (true) {
            case (props.hover==null):
                setRender(<div>Paspauskite ant grafiko dešinėje ir pamatysite palyginimą su kitais Lietuvos miestais</div>)
                break;
            case (props.hover==="Visų miestų indeksas"):
                setRender(
                    <div>
                        <div>
                            Visų miestų indeksas
                        </div>
                        <AllKPI></AllKPI>
                    </div>
                )
                break;
            
            default:
                break;
        }
    },[props.hover])
    console.log(data)

    return(
    <div>
        {render}
    </div>)
}
const AllKPI = () =>{
    const [data, setData] = useState(null)
    const [datasets, setDatasets] = useState(null)
    const spalvos = {
        Alytus:"#f94144",
        Klaipėda:"#f3722c",
        Vilnius: "#f8961e",
        Kaunas:"#f9c74f",
        Šiauliai:"#90be6d",
        Panevėžys:"#43aa8b"
    }
    useEffect(() => {
        fetch(
            "http://127.0.0.1:5000/kpi")
                        .then((res) => res.json())
                        .then((json) => {
                            setData(json)
                            let dataset = []
                            Object.keys(json).forEach(key => {
                                dataset.push({
                                    label: key,
                                    data: json[key].y,
                                    fill: false,
                                    backgroundColor: spalvos[key],
                                    borderColor: spalvos[key],
                                })
                              });
                            setDatasets(dataset)
                            
                        })
    },[])

    
    const options ={
        plugins:{
            legend:{

                position:"bottom",
            }
        }
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