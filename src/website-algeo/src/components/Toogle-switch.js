import React, { useState } from "react";
import './Toggle-switch.css'
const Toggle = () => {
    const [toggled,setToggled] = useState(false);
    
    const handleToggle = () => {
        setToggled(!toggled);
    };

    return (
        <div className="toogle">
            <button 
                onClick ={handleToggle} 
                className = {`toggle-btn ${toggled ? "toggled" : ""}`}>
                <div className="thumb">  </div>
            </button>
        </div>
    );
};

export default Toggle;