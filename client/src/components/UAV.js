import axios from "axios";
import React from 'react';
import UAVList from "./UAVList";

function UAV() {
    const [post, setPost] = React.useState([]);

    React.useEffect(() => {
        axios.get("http://localhost:8000/api/uav/").then((response) => {
            setPost(response.data);
        });
    }, []);

    return (
        <>
            <h1 className="text-center font-bold text-5xl my-5">UAV List</h1>
            <div className="flex flex-row">
                {post.map((post, index) => (
                    <UAVList key={index} posts={post}/>
                ))}
            </div>
        </>
    );
}

export default UAV;
