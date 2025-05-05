#!/bin/sh

echo "🔎 Verificando se há migrations pendentes..."

alembic current > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⏳ Nenhuma migration aplicada ainda. Rodando upgrade..."
    alembic upgrade head
else
    echo "✅ Migrations já estão atualizadas."
fi

echo "🚀 Iniciando o servidor Uvicorn..."
uvicorn main:app --host 0.0.0.0 --port 8000
