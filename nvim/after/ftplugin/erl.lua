vim.lsp.start {
  cmd = { '/usr/local/bin/erlang_ls' },
  root_dir = vim.fn.getcwd(), -- Use PWD as project root dir.
}
