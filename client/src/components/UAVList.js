
function UAVList(props) {
    return (
        <>
            <div className="basis-1/3 border-solid border-2 border-b-gray-600 mx-4">
                <h1 className="font-bold m-2">{"Name:   " + props.posts.name}</h1>
                <h1 className="font-bold m-2">{"Model:  " + props.posts.model.name}</h1>
                <h1 className="font-bold m-2">{"Model Created At:  " + props.posts.model.created_at}</h1>
                <h1 className="font-bold m-2">{"Weight:  " + props.posts.weight}</h1>
                <h1 className="font-bold m-2">{"Color:   " + props.posts.color}</h1>
            </div>
        </>
    );
}

export default UAVList;
