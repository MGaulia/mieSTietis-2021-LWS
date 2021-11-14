import React, { useEffect,useState } from "react";
import { Bar } from "react-chartjs-2";
const HomeCities = (props) =>{
    const [data, setData] = useState(null)
    useEffect(() => {

        
    },[])
    const dividerStyle = {borderTop:"3px solid", borderRadius:"5px", borderColor:"rgb(124, 128, 126)",
    margin:"0px 10px 0px 10px", marginLeft:"10px", marginRight:"10px"}
    return(
    <div style={{height:"670px", border:"2px solid",borderRadius:"5px", marginTop: "10px", marginBottom:"10px",
    display:"flex",flexDirection: "column"}}>
        <div style={{display:"flex", flexDirection:"row", justifyContent:"space-between", marginRight:"10px"}}>
            <div style={{paddingLeft:"10px",fontSize:"30px"}}>Visi Miestai</div>
            <div style={{paddingLeft:"10px",fontSize:"30px"}}>2020</div>
        </div>
        <hr className="" style={dividerStyle}></hr>
        <Barchartas thisCity={props.thisCity} group={"vanduo"}></Barchartas>
        <Barchartas thisCity={props.thisCity} group={"oras"}></Barchartas>
        <Barchartas thisCity={props.thisCity} group={"transportas"}></Barchartas>
        <Barchartas thisCity={props.thisCity} group={"siuksles"}></Barchartas>
        

    </div>)
}

const Barchartas = (props) => {
    const [datasets, setDatasets] = useState(null)
    
    
    
    useEffect(() => {
        const spalvos = {
            Alytus: props.thisCity==="Alytus"?"#78d975":"#72839c",
            Klaipėda:props.thisCity==="Klaipėda"?"#78d975":"#72839c",
            Vilnius: props.thisCity==="Vilnius"?"#78d975":"#72839c",
            Kaunas:props.thisCity==="Kaunas"?"#78d975":"#72839c",
            Šiauliai:props.thisCity==="Šiauliai"?"#78d975":"#72839c",
            Panevėžys:props.thisCity==="Panevėžys"?"#78d975":"#72839c"
        }
        fetch(
            "http://127.0.0.1:5000/catbar")
                        .then((res) => res.json())
                        .then((json) => {
                            let dataset = []
                            Object.keys(json).forEach(key => {
                                dataset.push({
                                    label: key,
                                    data: [json[key][props.group]],
                                    fill: false,
                                    backgroundColor: spalvos[key],
                                    borderColor: spalvos[key],
                                })
                              });
                            setDatasets(dataset)
                            
                        })
    }, [props.thisCity])
    

    const Icon = () => {
        const style1 = {position:"absolute", marginLeft:"370px", marginTop:"0px"}
        switch (true) {
            case (props.group==="vanduo"):
                return(<div>
                    <span style={style1}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-droplet" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M7.21.8C7.69.295 8 0 8 0c.109.363.234.708.371 1.038.812 1.946 2.073 3.35 3.197 4.6C12.878 7.096 14 8.345 14 10a6 6 0 0 1-12 0C2 6.668 5.58 2.517 7.21.8zm.413 1.021A31.25 31.25 0 0 0 5.794 3.99c-.726.95-1.436 2.008-1.96 3.07C3.304 8.133 3 9.138 3 10a5 5 0 0 0 10 0c0-1.201-.796-2.157-2.181-3.7l-.03-.032C9.75 5.11 8.5 3.72 7.623 1.82z"/>
                        <path fill-rule="evenodd" d="M4.553 7.776c.82-1.641 1.717-2.753 2.093-3.13l.708.708c-.29.29-1.128 1.311-1.907 2.87l-.894-.448z"/>
                    </svg>
                </span>
                </div>)
                break;
            case (props.group==="siuksles"):
                return(<div>
                    <span style={style1}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                    </svg>
                </span>
                </div>)
                break;
            case (props.group==="oras"):
                return(<div>
                    <span style={style1}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-clouds" viewBox="0 0 16 16">
                <path d="M16 7.5a2.5 2.5 0 0 1-1.456 2.272 3.513 3.513 0 0 0-.65-.824 1.5 1.5 0 0 0-.789-2.896.5.5 0 0 1-.627-.421 3 3 0 0 0-5.22-1.625 5.587 5.587 0 0 0-1.276.088 4.002 4.002 0 0 1 7.392.91A2.5 2.5 0 0 1 16 7.5z"/>
                <path d="M7 5a4.5 4.5 0 0 1 4.473 4h.027a2.5 2.5 0 0 1 0 5H3a3 3 0 0 1-.247-5.99A4.502 4.502 0 0 1 7 5zm3.5 4.5a3.5 3.5 0 0 0-6.89-.873.5.5 0 0 1-.51.375A2 2 0 1 0 3 13h8.5a1.5 1.5 0 1 0-.376-2.953.5.5 0 0 1-.624-.492V9.5z"/>
                </svg>
                </span>
                </div>)
                break;
            case (props.group==="transportas"):
                return(<div>
                    <span style={style1}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-minecart" viewBox="0 0 16 16">
                <path d="M4 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0 1a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm8-1a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0 1a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM.115 3.18A.5.5 0 0 1 .5 3h15a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 14 12H2a.5.5 0 0 1-.491-.408l-1.5-8a.5.5 0 0 1 .106-.411zm.987.82 1.313 7h11.17l1.313-7H1.102z"/>
                </svg>
                </span>
                </div>)
                break;
        
            default:
                break;
        }
    }
    const options = {
        plugins:{
            legend:{
                display:false,
            },
        },
        aspectRatio: 2.65,
        scales: {
            x:
                {
                    display:false
                }
            ,
            y: [
            
             {ticks: {mirror: true}}
            
          ],
        },
      };
    
     return(
        <>
        <div>
            {Icon()}
            {(datasets!==null)?<Bar data={{
            labels: [2020],
            datasets: datasets,
            }} options={options} />:null}
        </div>
        </>
      );
}

export default HomeCities