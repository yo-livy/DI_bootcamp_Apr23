import data from '../data.json';

const PostList = () => {

    return (
        <>
        <h2>Hi! This is a Title!</h2>
        {data.map((item) => {
                return (
                <div key={item.id}>
                    <h4>{item.title}</h4>
                    <h6>{item.content}</h6>
                </div>
                );
        })}
        </>
    );
};

export default PostList;