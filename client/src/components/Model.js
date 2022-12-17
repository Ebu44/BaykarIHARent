import axios from "axios";
import React from 'react';
import ModelList from "./ModelList";

function Model() {
    const [post, setPost] = React.useState([]);

    React.useEffect(() => {
        axios.get("http://localhost:8000/api/model/").then((response) => {
            setPost(response.data);
        });
    }, []);

    return (
        <>
            <h1 className="text-center font-bold text-5xl my-5">Model List</h1>
            <div className="flex flex-row">
                {post.map((post, index) => (
                    <ModelList key={index} posts={post}/>
                ))}
            </div>
        </>
    );
}

export default Model;
