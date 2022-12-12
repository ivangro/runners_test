until $(curl  --output ./output.txt --silent --head --fail http://localhost:3000/); do
    printf '.'
    sleep 5
done
