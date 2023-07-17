import './Exercise3.css';

const Exercise3 = () => {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };
    return (
        <>
        <h1 style={style_header}>This is a header</h1>
        <p className='para'>This is a paragraph</p>
        <a href='#'>This is a link</a>
        <form>
            <label for='name'>Enter your name:</label>
            <input id='name'></input>
            <button id='btn'>Submit</button>
        </form>
        <img src='https://images.unsplash.com/photo-1689457362806-af3a973a3c45?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2340&q=80' />
        <ul>This is a list:
            <li>Coffee</li>
            <li>Tea</li>
            <li>Milk</li>
        </ul>
        </>
        
    )
}

export default Exercise3;