require './models/post'

module MyApp
  class Application < Sinatra::Base
    configure do
      register Sinatra::ActiveRecordExtension
      set :database_file, 'config/database.yml'
    end

    configure :development do
      register Sinatra::Reloader
    end

    get '/' do
      @posts = Post.all
      erb :index
    end

    get '/new' do
      @post = Post.new
      erb :new
    end

    post '/' do
      @post = Post.create!(title: params[:title], contents: params[:contents])
      erb :create
    end
  end
end
