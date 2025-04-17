# deploy.sh
git pull
read -p "커밋 메시지를 입력하세요: " commit_message

git add .
git commit -m "$commit_message"
git push
