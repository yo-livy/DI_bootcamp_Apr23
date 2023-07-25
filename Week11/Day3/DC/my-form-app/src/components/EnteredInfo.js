const EnteredInfo = (props) => {
    console.log(props.formData.nutsFree)

    return (
        <>
        <h1>Enetred Information</h1>
        <h4>Your name: {props.formData.fName} {props.formData.lName}</h4>
        <h4>Your age: {props.formData.age}</h4>
        <h4>Your gender: {props.formData.gender}</h4>
        <h4>Your destination: {props.formData.country}</h4>
        <h4>Your dietery restrictions:</h4>
        <h5>**Nuts free: {props.formData.nutsFree ? 'Yes' : 'No'}</h5>
        <h5>**Lactose free: {props.formData.lactoseFree ? 'Yes' : 'No'}</h5>
        <h5>**Vegan: {props.formData.vegan ? 'Yes' : 'No'}</h5>
        </>
    );
};

export default EnteredInfo;