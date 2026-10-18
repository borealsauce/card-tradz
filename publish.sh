#!/bin/bash
set -e
cd /workspace/card_trade_demo
cp /workspace/shared/sortable.js ./sortable.js
git add -A && git commit -qm "${1:-Update demo}" || true
git push -q origin main
