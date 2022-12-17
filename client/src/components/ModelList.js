import Model from "./Model";

function ModelList(props) {
    return (
        <>
            <div className="basis-1/3 border-solid border-2 border-b-gray-600 mx-4">
                <h1 className="font-bold m-2">{"Name:   " + props.posts.name}</h1>
                <h1 className="font-bold m-2">{"Updated At:  " + props.posts.updated_at}</h1>
            </div>
        </>
    );
}

export default ModelList;
