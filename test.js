

const [count, setCount] = useState(0);

useEffect(() => {

  setCount(count + 1);

}, []);

console.log(count);


