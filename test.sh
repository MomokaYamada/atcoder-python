PYPY="pypy:3-2.4.0" # 旧ジャッジ
# PYPY="pypy:3-7.3.0" # 新ジャッジ

docker pull "$PYPY"

RUN="docker run -i --rm -v $PWD:/usr/src/myapp -w /usr/src/myapp $PYPY pypy3 Main.py"

echo "Removing old output..."
mkdir -p output
rm output/*

for file in `ls input`; do
    echo -n "Testing $file..."
    timeout 5 $RUN < input/$file > output/$file 2>&1
    if diff -q output/$file answer/$file > /dev/null; then
        echo "passed."
    else
        echo "failed."
    fi
done

for file in `ls input`; do
    bat output/$file
done
