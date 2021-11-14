import React, { useEffect,useState } from "react";
import { Line } from "react-chartjs-2";
const ExpandedCities = (props) =>{
    const [data, setData] = useState(null)
    const [render, setRender] = useState(null)
    useEffect(() => {
        let style1 ={fontSize:"20px", paddingLeft:"5px"}
        switch (true) {
            case (props.hover==null):
                setRender(<div
                style={{fontSize:"20px", textAlign:"center"}}>
                    Paspauskite ant grafiko kairėje ir pamatysite palyginimą su kitais Lietuvos miestais</div>)
                break;
            case (props.hover==="Visų miestų indeksas"):
                setRender(
                    <div>
                        <div style={style1}>
                            Visų miestų indeksas
                        </div>
                        <AllKPI group={"kpi"}></AllKPI>
                    </div>
                )
                break;
            case (props.hover==="Viešojo transoporto įvertinimas"):
                setRender(
                    <div>
                        <div style={style1}>
                            Viešojo transoporto įvertinimas
                        </div>
                        <AllKPI group={"transportas"}></AllKPI>
                    </div>
                )
                break;
            case (props.hover==="Oro taršos mažinimo indeksas"):
                setRender(
                    <div>
                        <div style={style1}>
                            Oro taršos mažinimo indeksas
                        </div>
                        <AllKPI group={"oras"}></AllKPI>
                    </div>
                )
                break;
            case (props.hover==="Vandens suvartojimo įvertinimas"):
                setRender(
                    <div>
                        <div style={style1}>
                            Vandens suvartojimo įvertinimas
                        </div>
                        <AllKPI group={"vanduo"}></AllKPI>
                    </div>
                )
                break;
            case (props.hover==="Atliekų įvertinimas"):
                setRender(
                    <div>
                        <div style={style1}>
                            Atliekų įvertinimas
                        </div>
                        <AllKPI group={"siuksles"}></AllKPI>
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
const AllKPI = (props) =>{
    const [data, setData] = useState(null)
    const [datasets, setDatasets] = useState(null)
    const spalvos = {
        Alytus:"#5778a4",
        Klaipėda:"#d1615d",
        Vilnius: "#e7ca60",
        Kaunas:"#e49444",
        Šiauliai:"#6a9f58",
        Panevėžys:"#85b6b2"
    }
    useEffect(() => {

        fetch(
            "http://127.0.0.1:5000/"+props.group)
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
    },[props.group])

    
    const options ={
        aspectRatio:1.5,
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