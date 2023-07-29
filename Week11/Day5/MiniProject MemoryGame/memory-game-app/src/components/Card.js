import './Card.css'

const Card = (props) => {

    return (
        <div className="card">
            <div className="img-container">
                <img src={props.img} alt=""/>
            </div>
            <div className='title'>
                <p><b>Name:</b>{props.name}</p>
                <p><b>Occuptaion:</b>{props.occupation}</p>
            </div>
            
        </div>
      
    );
};

export default Card;